import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var questions = [
      'What\'s your facvorite color',
      'What\'s your favorite animal'
    ];
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Something'),
        ),
        body: Column(children: <Widget>[
          Text(questions[0]),
          TextButton(onPressed: null, child: Text('something'))
        ]),
      ),
    );
  }
}
