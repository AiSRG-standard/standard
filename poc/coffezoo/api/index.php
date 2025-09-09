<?php
// Set the content type to JSON for all responses
header('Content-Type: application/json');

// Get the request method
$method = $_SERVER['REQUEST_METHOD'];

// A simple router based on the request method
switch ($method) {
    case 'GET':
        handle_get_request();
        break;
    case 'POST':
        handle_post_request();
        break;
    default:
        // Handle unsupported methods
        header('HTTP/1.1 405 Method Not Allowed');
        echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
        break;
}

function handle_get_request() {
    // For this PoC, we assume any GET request is for the menu
    $response = [
        'status' => 'success',
        'menu_items' => 'Latte, Americano, Croissant, Cheesecake'
    ];
    echo json_encode($response);
}

function handle_post_request() {
    // Get the JSON payload from the request body
    $json_payload = file_get_contents('php://input');
    $data = json_decode($json_payload, true);

    // For this PoC, we assume any POST request is for booking a table.
    // In a real application, you would check a parameter like 'action' or have different endpoints.
    
    // Check if required data is present (basic validation)
    if (isset($data['date']) && isset($data['time']) && isset($data['guests'])) {
        
        // Simulate a successful booking
        $booking_id = rand(1000, 9999); // Generate a random booking ID
        
        $response = [
            'status' => 'success',
            'booking_id' => $booking_id,
            'date' => htmlspecialchars($data['date']),
            'time' => htmlspecialchars($data['time']),
            'guests' => (int)$data['guests']
        ];
        
        echo json_encode($response);
        
    } else {
        // Handle missing data
        header('HTTP/1.1 400 Bad Request');
        echo json_encode([
            'status' => 'error', 
            'error_message' => 'Missing required parameters (date, time, guests).'
        ]);
    }
}

?>