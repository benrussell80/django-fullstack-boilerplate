import React from 'react';
import { Route } from "react-router-dom";
import { NoMatch } from "./components";


export default [
  <Route path="*" component={NoMatch} key="404" />
]