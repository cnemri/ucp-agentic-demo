#!/bin/bash

# Terminate background processes on exit
cleanup() {
  echo ""
  echo "Stopping services..."
  kill "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null
  exit
}

trap cleanup INT TERM

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check for GOOGLE_API_KEY
if [ -f business_agent/.env ]; then
  export $(grep -v '^#' business_agent/.env | xargs)
fi

if [ -z "$GOOGLE_API_KEY" ]; then
  echo "Error: GOOGLE_API_KEY is not set. Please set it in business_agent/.env or export it."
  exit 1
fi

echo "Starting backend (Cymbal Retail Agent)..."
cd business_agent
uv run business_agent > "$SCRIPT_DIR/backend.log" 2>&1 &
BACKEND_PID=$!
cd "$SCRIPT_DIR"

echo "Starting frontend (Chat Client)..."
cd chat-client
npm run dev > "$SCRIPT_DIR/frontend.log" 2>&1 &
FRONTEND_PID=$!
cd "$SCRIPT_DIR"

# Wait a second to check if processes are still running
sleep 2

if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
  echo "Error: Backend failed to start. Check backend.log for details."
  cleanup
fi

if ! kill -0 "$FRONTEND_PID" 2>/dev/null; then
  echo "Error: Frontend failed to start. Check frontend.log for details."
  cleanup
fi

echo "------------------------------------------------"
echo "Demo is running!"
echo "- React Frontend: http://localhost:3000"
echo "- Agent Backend:  http://localhost:10999"
echo "- Log files:      backend.log, frontend.log"
echo "------------------------------------------------"
echo "Press Ctrl+C to stop both servers."

# Keep script running to wait for background jobs
wait
