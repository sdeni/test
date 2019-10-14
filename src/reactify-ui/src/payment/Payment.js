import React, {Component} from 'react';
import 'whatwg-fetch'
import cookie from "react-cookies";


class Payment extends Component {

    createPost(data) {
        const endpoint = '/list/';
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;
        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data),
                credentials: 'include'
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                console.log(responseData)

            }).catch(function (error) {
                console.log("error", error);
                alert("An error occured, please try again later.")
            })
        }
    }



    render() {
        return (
            <div>
                <h1>Payment pagesssssss</h1>
            </div>
        );
    }
}

export default Payment;
