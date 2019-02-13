//
//  Hello World server in C++
//  Binds REP socket to tcp://*:5555
//  Expects "Hello" from client, replies with "World"
//
#include <zmq.hpp>
#include <string>
#include <iostream>
#ifndef _WIN32
#include <unistd.h>
#else

#include <windows.h>
#define sleep(n)	Sleep(n)
#endif

int main () {
    //  Prepare our context and socket
    zmq::context_t context (1);
    zmq::socket_t socket (context, ZMQ_PULL);
    socket.connect ("tcp://127.0.0.1:5555");

    while (true) {
        zmq::message_t message;
        //  Wait for next message from client
        socket.recv (&message);
        std::cout << "Received message size in bytes " << message.size() << std::endl;

    }
    return 0;
}