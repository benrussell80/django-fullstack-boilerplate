import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import { Header } from '../../../common';


const Detail = ({ author, title, bannerUrl, body, numberOfLikes, publishedAt, comments }) => {
  const dateOptions = {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  };

  let publishedAtString = new Date(publishedAt).toLocaleDateString('en-US', dateOptions);

  console.log(author, title, bannerUrl, body, numberOfLikes, publishedAt, publishedAtString, comments);
  

  return (
    <Container>
      <Header>{title}</Header>
      <Row>
        <h4>Author: {author.username}</h4>
        <h5><i> - {publishedAtString}</i></h5>
        <h5>Likes: {numberOfLikes}</h5> {/* add in like button */}
      </Row>
      <Row>
        <div className='text-center'>
          {bannerUrl === '' ? '' : <img src={bannerUrl} alt={`${title}-banner`} />}
        </div>
      </Row>
      <Row>
        <Col>
          <p className='lead'>{body}</p>
        </Col>
      </Row>
    </Container>
  );
}

export default Detail;