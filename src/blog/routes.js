import React from 'react';
import { Route } from "react-router-dom";
// import { ListContainer } from './components/List';
import { DetailContainer } from './components/Detail';

export default [
  // <Route path="/posts/" exact component={ListContainer} key="blog-posts" />,
  <Route path="/post/:slug/" exact component={DetailContainer} key="blog-post-detail" />,
];