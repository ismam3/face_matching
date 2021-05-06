import React from 'react';

function Header(props) {
    return (
        <div className="header" style={{background:'pink'}}>
            <div style={{display:'inline-flex'}}>
                <img style={{width:'50px',height:'50px'}} alt="Ismam Labib" src={process.env.PUBLIC_URL + '/icn.png'}></img>
                <h1>Face matching application</h1>
            </div>
        </div>
    );
}

export default Header;