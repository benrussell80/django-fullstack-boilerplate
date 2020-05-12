import React from 'react';


export const Header = (props) => {
  return (
    <div className="header">
      <div className="w-100"><hr /></div>
      <div className="mx-auto">
        <h2 className="text-center">
          {props.children}
        </h2>
      </div>
      <div className="w-100"><hr /></div>
    </div>
  );
}