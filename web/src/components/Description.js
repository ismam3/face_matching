import React from 'react';
import {Image} from 'react-bootstrap'
import Download from './Download';

function Description(props) {
    return (
        <div>
            <Download></Download>
            <div>
                <h2>Confused to find Selena and Lucy?</h2>
                <Image src="https://drive.google.com/uc?id=1Bx9nVPf44OUPAvWighK1SPGyzp-q4ylP" thumbnail></Image>
            </div>
            <div>
                <h3>Then Use me!</h3>
                <Image src="https://drive.google.com/uc?id=1OJYhG2-r79QsmcQ2VBXHvluek1Ed5HF3" thumbnail></Image>
            </div>
            <div>
                <h5>Select two pictures with cute faces and compare the!!<br></br>Done</h5>
                <Image src="https://drive.google.com/uc?id=15yK11pI6lnbb3Y1415wtP3Os2oU4Urrl" thumbnail></Image>
            </div>
        </div>
    );
}

export default Description;