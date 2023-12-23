<?php
header('Content-Type: application/json');

$data = json_decode(file_get_contents('php://input'), true);

if (isset($data['name']) && isset($data['email']) && isset($data['message'])) {
  $name = $data['name'];
  $email = $data['email'];
  $message = $data['message'];
  $to = 'itemggroup@gmail.com'; 
  $subject = 'Feedback from ' . $name;
  $body = "Name: $name\nEmail: $email\nMessage: $message";
  $headers = "From: $email";

  if (mail($to, $subject, $body, $headers)) {
    http_response_code(200);
    echo json_encode(array("message" => "Your feedback has been received. Thank you!"));
  } else {
    http_response_code(500);
    echo json_encode(array("message" => "Our support team isn't available. Please try again later."));
  }
} else {
  http_response_code(400);
  echo json_encode(array("message" => "Incomplete data received. Please fill in all fields."));
}
?>
