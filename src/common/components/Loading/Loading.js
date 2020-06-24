import React from 'react';
import { Container, Col, Row, Spinner } from 'reactstrap';


const Loading = () => {
  return (
    <Container>
      <Row>
        <Col md={{ size: 4, offset: 4 }} className="text-center py-4">
          <Spinner />
        </Col>
      </Row>
    </Container>
  );
}

export default Loading;