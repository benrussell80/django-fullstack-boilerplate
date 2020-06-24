import React from 'react';
import { Container, Row, Col, Card, CardHeader, CardBody, CardFooter, Button, Spinner } from 'reactstrap';
import { Header } from '../../../common';
import { formatDate } from '../../../utils';


const Detail = ({ author, title, bannerUrl, body, numberOfLikes, publishedAt, comments, loadMoreComments, loadingMoreComments }) => {
  return (
    <Container>
      <Header>{title}</Header>
      <Row>
        <Col>
          <h4>Author: {author.username}<i> - {formatDate(publishedAt)}</i></h4>
          <h5>Likes: {numberOfLikes}</h5> {/* add in like button */}
        </Col>
      </Row>
      <Row>
        <Col>
          <div className='text-center'>
            {bannerUrl === '' ? '' : <img width="100%" src={bannerUrl} alt={`${title}-banner`} />}
          </div>
        </Col>
      </Row>
      <Row>
        <Col md={{ size: 8, offset: 2 }}>
          <p className='lead'>{body}</p>
        </Col>
      </Row>
      <Row>
        <Col md={{ size: 8, offset: 2 }}>
          <Header>Comments</Header>
          {comments.edges.map(({ node: comment }, index) => {
            return (
              <div key={`Detail-Comments-container-${index}`} className="py-2">
                <Card key={`Detail-Comments-Card-${index}`}>
                  <CardHeader key={`Detail-Comments-CardHeader-${index}`} className="clearfix">
                    <span key={`Detail-Comments-username-span-${index}`} className="float-left"><strong key={`Detail-Comments-username-strong-${index}`}>{comment.author.username}</strong></span>
                    <span key={`Detail-Comments-date-span-${index}`} className="float-right"><i key={`Detail-Comments-date-i-${index}`}>{formatDate(comment.createdAt)}</i></span>
                  </CardHeader>
                  <CardBody key={`Detail-Comments-CardBody-${index}`}>{comment.body}</CardBody>
                  <CardFooter key={`Detail-Comments-CardFooter-${index}`} className="clearfix">
                    <span key={`Detail-Comments-likes-span-${index}`} className="float-right">Likes: {comment.numberOfLikes}</span>
                  </CardFooter>
                </Card>
              </div>
            );
          })}
          {/* state for loading more comments -> "Load more comments" if false, ~spinner~ if true */}
          <Button color="info" block className="py-2" onClick={loadMoreComments}>{loadingMoreComments ? <Spinner /> : "Load More Comments"}</Button>
        </Col>
      </Row>
    </Container>
  );
}

export default Detail;