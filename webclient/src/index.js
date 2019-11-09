import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import "./style.css";

const App = props => {
    const [state, setState] = useState(0);

    return (
        <main>
            {state ? <div/> : "Hello there"}
        </main>
    )
}

ReactDOM.render(<App />, document.getElementById('root'));

