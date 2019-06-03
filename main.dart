import 'dart:convert';
import 'dart:io';

void main() async{
  var url = 'http://127.0.0.1:8000/notex/signIn/?password=helloxssss&username=skullcrushersss';
    var request = await HttpClient().postUrl(Uri.parse(url));

  // sends the request
  var response = await request.close(); 

  // transforms and prints the response
  await for (var contents in response.transform(Utf8Decoder())) {
    print(contents);
  }
}