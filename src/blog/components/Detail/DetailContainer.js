import React, { Component } from 'react';
import axios from 'axios';
import { Detail } from '.';
import { withRouter } from 'react-router-dom';
import { NoMatch } from "../../../errors/components";


class DetailContainer extends Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
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
              comments {
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
        this.setState({ ...response.data.data.post.edges[0].node });
      })
      .catch(error => {
        this.setState({ error });
      })
  }

  loadMoreComments() {
    // function for loading more comments with relay pagination
  }

  render() {
    if (this.state.published && this.state.error === null) {
      document.title = this.state.title === '' ? this.state.slug : this.state.title;
      return (
        <Detail {...this.state} />
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