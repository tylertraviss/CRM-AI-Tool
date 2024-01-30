import React from 'react';
import Card from 'react-bootstrap/Card';

function CardEntity({ title, subtitle, text }) {
  return (
    <Card style={{ width: '40rem' }}>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">{subtitle}</Card.Subtitle>
        <Card.Text style={{ fontSize: '0.8em' }}>
          {text}
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default CardEntity;
