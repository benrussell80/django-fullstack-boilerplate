import React, { Component } from 'react';
import axios from 'axios';
import { Detail } from '.';
import { withRouter } from 'react-router-dom';
import { NoMatch } from '../../../errors/components';
import { Loading } from '../../../common/components/Loading'


class DetailContainer extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loaded: false,
      errors: null,
      loadingMoreComments: false,
      id: '',
      author: {
        username: '',
      },
      title: '',
      bannerUrl: '',
      body: '',
      numberOfLikes: 0,
      slug: this.props.match.params.slug,
      published: false,
      publishedAt: '',
      comments: {
        edges: [],
        pageInfo: {}
      }
    }
    this.loadMoreComments = this.loadMoreComments.bind(this);
  }

  componentDidMount() {
    axios.post('/graphql/', {
      query: `
      query PostDetail($slug: String!) {
        posts(slug: $slug, first: 1) {
          edges {
            node {
              id
              author {
                username
              }
              title
              bannerUrl
              body
              numberOfLikes
              published
              publishedAt
              comments(first: 5) {
                pageInfo {
                  hasNextPage
                }
                edges {
                  node {
                    id
                    author {
                      username
                    }
                    body
                    numberOfLikes
                    createdAt
                  }
                }
              }
            }
          }
        }
      }`,
      variables: { slug: this.state.slug }
    })
      .then(response => {
        this.setState({ loaded: true })
        this.setState({ ...response.data.data.posts.edges[0].node });
      })
      .catch(error => {
        this.setState({ error });
      })
  }

  loadMoreComments() {
    console.log('Loading more comments');
    this.setState({ loadingMoreComments: true })
    
    // function for loading more comments with relay pagination
  }

  render() {
    if (this.state.loaded === false) {
      document.title = 'Loading...';
      return (
        <Loading />
      )
    } else if (this.state.published) {
      document.title = this.state.title === '' ? this.state.slug : this.state.title;
      return (
        <Detail {...this.state} loadMoreComments={this.loadMoreComments} />
      )
    } else {
      document.title = 'No Match';
      return (
        <NoMatch />
      )
    }
  }
}

export default withRouter(DetailContainer);