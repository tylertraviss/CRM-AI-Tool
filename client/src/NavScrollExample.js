// NavScrollExample.js
import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

function NavScrollExample() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      {/* Add fluid property to make the container full-width */}
      <Container fluid>
        <Navbar.Brand href="#">CRM Tool</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav className="me-auto" navbarScroll>
            <Nav.Link href="#home">Dashboard</Nav.Link>
            <Nav.Link href="#about">Clients</Nav.Link>
            <Nav.Link href="#contact">Sales</Nav.Link>
          </Nav>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavScrollExample;
