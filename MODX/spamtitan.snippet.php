<?php
/* SpamTitan Free FormIt Hook 
* Created By AlphaToro 
* https://github.com/alpha-toro/spam-titan-free
*/

$formFields = $hook->getValues();
$email = $formFields['email'];
$message = $formFields['message'];

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://XXXXX.azurewebsites.net/spam', //change to your cloud server
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json'
  ),
  CURLOPT_POSTFIELDS =>'{"message":"'.$message.'","email":"'.$email.'"}'
));

$response = json_decode(curl_exec($curl));

curl_close($curl);

if($response->status == 400){
    if($response->message){
        $hook->addError('message',$response->message);
    }
    if($response->email){
        $hook->addError('email',$response->email);
    }
    return false;
} else {
    return true;
}