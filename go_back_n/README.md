# Go-Back-N ARQ Implementation

Simulation of the Go-Back-N sliding window protocol over an unreliable channel with configurable packet loss, ACK loss, and data corruption.

## Algorithm

### Sender
```text
NextSeqNum = 0
Base = 0
for each message (up to window size from Base):
    send(message, NextSeqNum)
    NextSeqNum++
on ACK(seq) received:
    Base = seq + 1
    if Base < NextSeqNum:
        restart timer
on timeout:
    retransmit all frames from Base to NextSeqNum - 1
```

### Receiver
```text
ExpectedSeqNum = 0
on frame(seq, data) received:
    if not corrupted and seq == ExpectedSeqNum:
        accept(data)
        send ACK(seq)
        ExpectedSeqNum++
    else if seq < ExpectedSeqNum:
        send ACK(seq)   // duplicate
    else:
        discard (out of order)
```

## Project Structure
- `main.py`: Simulation orchestrator and entry point.
- `models.py`: `Frame`/`Ack` dataclasses and configuration constants.
- `channel.py`: Unreliable channel with probabilistic loss and corruption.
- `sender.py`: Sender logic — sliding window, timeout, bulk retransmission.
- `receiver.py`: Receiver logic — in-order acceptance, duplicate/out-of-order handling.

## How to Run
```bash
python main.py
```
