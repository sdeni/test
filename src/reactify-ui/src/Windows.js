import React, { Component } from 'react';
import Modal from './Modals/Modal';

class Windows extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
  }

  toggleModal = () => {
    this.setState({
      isOpen: !this.state.isOpen
    });
  };

  render() {
    return (
      <div className="App">
          <a onClick={this.toggleModal} className="navbar-brand text-success">Open the modal</a>
        <Modal show={this.state.isOpen}
          onClose={this.toggleModal}>
          Here's some content for the modal
        </Modal>
      </div>
    );
  }
}

export default Windows;