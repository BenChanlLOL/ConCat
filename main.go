package main

import (
	"fmt"
	"net"
	"strings"
)

func main() {
	// Prompt the user for IP address and port
	fmt.Println("Enter an IP address to connect to (e.g., google.com:443) or 'help' for other options:  ")
	var input string
	fmt.Scanln(&input)

	if input == "bind" {
		// Start a server
		fmt.Println("Starting server on port 7092...")
		ln, err := net.Listen("tcp", ":7092")
		if err != nil {
			fmt.Println("Error binding to port:", err)
			return
		}
		defer ln.Close()

		for {
			conn, err := ln.Accept()
			if err != nil {
				fmt.Println("Error accepting connection:", err)
				continue // Continue waiting for new connections
			}
			defer conn.Close()

			// Handle incoming connection in a separate goroutine
			go handleConnection(conn)
		}
	} else if input == "version" {
		// print version
		fmt.Println("version 0.2.2(go beta version)")

	} else if input == "help" {
		// give help
		fmt.Println("version - displays the version")
		fmt.Println("bind - starts a tcp server on port 7092")

	} else {
		// Connect as a client
		var serverAddr string
		if !strings.Contains(input, ":") {
			// Default port if not specified
			serverAddr = fmt.Sprintf("%s:443", input)
		} else {
			serverAddr = input
		}

		conn, err := net.Dial("tcp", serverAddr)
		if err != nil {
			fmt.Println("Error connecting to server:", err)
			return
		}
		defer conn.Close()

		// Send/receive data in a loop
		for {
			var data string
			fmt.Println("Enter data to send (or 'exit' to quit):")
			fmt.Scanln(&data)

			if data == "exit" {
				break
			}

			_, err = conn.Write([]byte(data))
			if err != nil {
				fmt.Println("Error sending data:", err)
				break
			}

			
		}
	}
}

func handleConnection(conn net.Conn) {
	// Handle data received from the client connection

	defer conn.Close() // Ensure connection is closed even if errors occur
}
