#!/bin/bash -e

script_dir=$(dirname "$0")
daemon_pid_file="$script_dir"/.socket.daemon.pid

HOST="localhost"
PORT="8000"

run() {
	"$script_dir"/main.py -p "$PORT" -H "$HOST"
}

run_daemon() {
	"$script_dir"/main.py -p "$PORT" -H "$HOST" &
	pid=$!
	echo "Run daemon with pid: $pid"
	echo "$pid" >"$daemon_pid_file"
}

kill_daemon() {
	pid=$(cat "$daemon_pid_file")
	kill -9 "$pid"
	wait $!
	rm "$daemon_pid_file"
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
