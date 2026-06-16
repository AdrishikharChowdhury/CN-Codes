# Selective Repeat ARQ Implementation

Simulation of the Selective Repeat sliding window protocol over an unreliable channel. Unlike Go-Back-N, only lost or timed-out frames are retransmitted, and the receiver buffers out-of-order frames.

## Algorithm

### Sender
```text
Base = 0, NextSeqNum = 0
for each message (up to window size from Base):
    send(message, NextSeqNum)
    start timer for NextSeqNum
    NextSeqNum++
on ACK(seq) received:
    mark seq as acked
    cancel timer for seq
    while Base is acked:
        slide window, Base++
on timeout for seq:
    retransmit only seq
    restart timer for seq
```

### Receiver
```text
Base = 0
buffer = {}
on frame(seq, data) received:
    if seq < Base:
        resend ACK(seq)
    else if seq >= Base + window_size:
        drop
    else:
        buffer[seq] = data
        send ACK(seq)
        while Base in buffer:
            deliver buffer[Base]
            Base++
```

## Project Structure
- `main.py`: Simulation orchestrator and entry point.
- `models.py`: `Frame`/`Ack` dataclasses and configuration constants.
- `channel.py`: Unreliable channel with probabilistic loss and corruption.
- `sender.py`: Sender logic — per-frame timers, selective retransmission.
- `receiver.py`: Receiver logic — out-of-order buffering, in-sequence delivery.

## How to Run
```bash
python main.py
```
