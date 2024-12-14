#!/bin/bash -e

script_dir=$(dirname "$0")

HOST="localhost"
PORT="8000"

run() {
	"$script_dir"/main.py -p "$PORT" -H "$HOST"
}

run_daemon() {
	"$script_dir"/main.py -p "$PORT" -H "$HOST" &
	pid=$!
	echo "Run daemon with pid: $pid"
	echo "$pid" >/tmp/.socket.daemon.pid
}

kill_daemon() {
	pid=$(cat /tmp/.socket.daemon.pid)
	kill -9 "$pid"
	wait $!
	rm /tmp/.socket.daemon.pid
}

ping() {
	curl http://localhost:8000
}

case $1 in
"run" | "r")
	run
	;;
"run_daemon" | "rd")
	run_daemon
	;;
"kill" | "k")
	kill_daemon
	;;
"ping" | "p")
	ping
	;;
*)
	echo "Unknown command: $1"
	exit 1
	;;
esac
