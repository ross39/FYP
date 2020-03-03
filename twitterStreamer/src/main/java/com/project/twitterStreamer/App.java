package com.project.twitterStreamer;


import com.project.twitterStreamer.producer.TwitterKafkaProducer;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        TwitterKafkaProducer producer = new TwitterKafkaProducer();
        producer.run();
    }
}
