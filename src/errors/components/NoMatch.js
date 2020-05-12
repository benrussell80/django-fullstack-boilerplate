import React from 'react';
import { Col, Container, Row } from 'reactstrap'
import { useLocation } from 'react-router-dom';
import { Header } from '../../common';


const NoMatch = () => {
  let location = useLocation();

  return (
    <Container>
      <Row>
        <Col>
          <Header>
            {'No match for '}<code>{location.pathname}</code>
          </Header>
        </Col>
      </Row>
    </Container>
  );
}

export default NoMatch;