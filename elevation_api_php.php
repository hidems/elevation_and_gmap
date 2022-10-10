<?php
// API URL
$url = 'https://api.opentopodata.org/v1/etopo1?locations=39.747114,-104.996334';

// Create a new cURL resource
$options = array(
    // HTTP context option
    'http' => array(
        'method'=> 'GET',
        'header'=> 'Content-type: application/json; charset=UTF-8' //JSON形式で表示
    )
);

// Stream context
$context = stream_context_create($options);

$raw_data = file_get_contents($url, false,$context);

// debug
var_dump($raw_data);