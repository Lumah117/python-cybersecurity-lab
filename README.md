# Python Cybersecurity Lab

A collection of Python cybersecurity and networking experiments developed during my university studies.

The project explores several concepts including HTTP/HTTPS proxy behaviour, web-traffic handling, local webcam and microphone capture, multimedia processing and concurrent programming.

The scripts were created as educational proof-of-concept exercises within a controlled laboratory environment.

> **Ethical use:** This repository is provided for educational and portfolio purposes. Network-security experiments should only be performed on systems and networks that you own or have explicit permission to test.

---

## Project Overview

The recovered project can broadly be divided into two areas:

```text
Python Cybersecurity Lab
│
├── Network / Proxy Experiments
│   ├── HTTP proxying
│   ├── HTTPS request handling
│   ├── URL rewriting
│   ├── Domain targeting
│   └── mitmproxy experimentation
│
└── Multimedia Capture
    ├── Microphone recording
    ├── Webcam capture
    ├── Still-image capture
    ├── Video recording
    └── Concurrent audio/video capture
```

These scripts represent experimental coursework rather than production security tooling.

---

## Technologies

- Python
- HTTP
- HTTPS
- Python `http.server`
- `socketserver`
- `requests`
- `urllib`
- mitmproxy
- OpenCV
- PyAudio
- WAV audio processing
- NumPy
- Python threading

---

## Repository Structure

```text
python-cybersecurity-lab/
│
├── README.md
├── LICENSE
│
└── src/
    ├── proxy_experiments/
    │   ├── Downgrade_https.py
    │   ├── Downgrade_Targeted.py
    │   └── Downgrade_Test.py
    │
    └── multimedia_capture/
        ├── Ears.py
        ├── Eyes.py
        ├── Eyes_&_Ears.py
        └── Spy_Script.py
```

The original filenames have been retained to preserve the coursework implementation.

---

# Network and Proxy Experiments

Several scripts explore the behaviour of HTTP and HTTPS traffic through intermediary proxy software.

These experiments helped develop an understanding of:

- HTTP requests and responses
- HTTPS
- Proxy servers
- URL construction
- Redirect responses
- Request modification
- Response modification
- Web-security mechanisms
- Man-in-the-middle concepts
- The importance of encrypted transport

---

## Basic Proxy Experiment

`Downgrade_https.py` implements an experimental HTTP server using Python's:

```python
http.server
socketserver
```

The server receives an incoming request and constructs the corresponding HTTPS resource.

Conceptually:

```text
Client Request
      |
      v
 Python Proxy
      |
      v
 HTTPS Request
      |
      v
 Remote Server
      |
      v
 HTTPS Response
      |
      v
 Proxy Processing
      |
      v
 Client Response
```

The returned HTML is processed by replacing HTTPS URL strings with HTTP equivalents.

This was an educational experiment intended to investigate the relationship between HTTP, HTTPS and intermediary proxy behaviour.

---

## Targeted Proxy Experiment

`Downgrade_Targeted.py` expands the proxy concept by introducing a list of selected domains.

The script checks the HTTP `Host` header against the configured domain list.

```text
Incoming Request
       |
       v
Read Host
       |
       v
Target Domain?
   /        \
 Yes         No
  |           |
  v           v
Construct    Return
HTTP URL     Default Page
  |
  v
302 Redirect
```

The implementation also uses Python's URL parsing functionality to separate the path and query components before constructing the resulting URL.

This provided experience with:

- HTTP headers
- Host identification
- URL parsing
- Query strings
- HTTP status codes
- Redirect responses

---

## mitmproxy Experiment

`Downgrade_Test.py` explores the same general concept using `mitmproxy`.

Rather than implementing the complete HTTP server directly, the script defines a mitmproxy request hook.

```text
HTTP Flow
    |
    v
Inspect Host
    |
    v
Configured Test Domain?
    |
   Yes
    |
    v
Inspect Scheme
    |
    v
Request Processing
```

This introduced the concept of using a specialised interception framework to inspect and manipulate HTTP flows.

---

# Why HTTPS Matters

These experiments also demonstrate why modern HTTPS protections are important.

At a conceptual level:

```text
HTTP

Client -------- Plain HTTP -------- Server
                  ^
                  |
          Traffic may be exposed


HTTPS

Client ===== Encrypted TLS ===== Server
                  ^
                  |
          Protected transport
```

Modern web security also includes mechanisms intended to prevent or limit protocol-downgrade attacks.

The project therefore serves primarily as an educational exploration of network-security concepts rather than a demonstration of a generally applicable attack against modern HTTPS websites.

---

# Microphone Capture

`Ears.py` implements local microphone recording using PyAudio.

The recording configuration includes:

```text
Channels:     1
Sample Rate:  44,100 Hz
Sample Type:  16-bit
Output:       WAV
```

Conceptually:

```text
Microphone
    |
    v
 PyAudio
    |
    v
Audio Stream
    |
    v
Frame Buffer
    |
    v
 WAV File
```

Audio samples are collected into a frame buffer before being written to a WAV file using Python's `wave` module.

---

# Webcam Capture

`Eyes.py` provides local webcam capture using OpenCV.

The script supports two modes:

```text
CAPTURE_MODE
│
├── video
│
└── image
```

### Video Mode

Video mode:

```text
Webcam
   |
   v
OpenCV
   |
   v
Capture Frames
   |
   v
VideoWriter
   |
   v
AVI File
```

The recovered implementation records frames at a configured resolution of:

```text
640 × 480
```

and writes them using an XVID video codec.

### Image Mode

Alternatively, the program can capture a single webcam frame and save it as an image.

```text
Webcam
   |
   v
Capture Frame
   |
   v
JPEG Image
```

---

# Concurrent Audio and Video

The combined multimedia scripts integrate the microphone and webcam functionality.

Two Python threads are created:

```text
               Main Program
                    |
          +---------+---------+
          |                   |
          v                   v
    Audio Thread         Video Thread
          |                   |
          v                   v
     Microphone             Webcam
          |                   |
          v                   v
      WAV File             AVI File
```

Both threads are started before the main program waits for them to complete.

This allowed audio and video acquisition to take place concurrently rather than recording one source followed by the other.

---

# Threading

The multimedia component provided practical experience with concurrent execution.

Without threading:

```text
Record Audio
     |
     v
Finish Audio
     |
     v
Record Video
```

With threading:

```text
        START
          |
     +----+----+
     |         |
     v         v
   Audio     Video
     |         |
     +----+----+
          |
          v
        FINISH
```

This is particularly useful when several independent I/O operations need to occur during the same period.

---

# Concepts Demonstrated

This project provided practical experience with:

- Python
- Computer networking
- HTTP and HTTPS concepts
- Proxy servers
- Request/response handling
- HTTP redirects
- URL parsing
- Network-security concepts
- mitmproxy
- OpenCV
- Webcam acquisition
- Image capture
- Video encoding
- PyAudio
- Audio acquisition
- WAV file generation
- Concurrent programming
- Python threads
- Resource management

---

# Original Implementation

The scripts in this repository preserve experimental university work.

They should not be interpreted as production-ready cybersecurity tools.

Some experiments make simplifying assumptions and modern web-security controls may prevent the behaviour being explored.

The original implementations are retained because they demonstrate the concepts I was learning at the time rather than being rewritten to appear representative of my current software-development practices.

---

# Responsible Use

Cybersecurity techniques can have legitimate educational and defensive applications but can also affect the privacy and security of other users.

The examples in this repository are intended only for:

- Controlled laboratory environments
- Personally owned systems
- Authorised security testing
- Cybersecurity education
- Defensive research

No captured personal data, credentials, private communications or test recordings are included in the repository.

---

# Retrospective

Reviewing this project with my later software and engineering experience highlights several areas that I would approach differently.

## Controlled Test Environment

Rather than experimenting against arbitrary external websites, I would now construct a dedicated local laboratory environment.

For example:

```text
Test Client
     |
     v
Local Network
     |
     v
Test Proxy
     |
     v
Local Test Web Server
```

This provides a repeatable environment in which network behaviour can be investigated without involving third-party systems.

---

## Clearer Separation of Components

The project could also be separated into reusable modules:

```text
Application
│
├── Network
│   ├── Proxy
│   ├── Request Handling
│   └── Response Processing
│
├── Audio
│   ├── Capture
│   └── Storage
│
└── Video
    ├── Capture
    └── Storage
```

This would make individual components easier to test and reuse.

---

## Configuration

Values such as:

- Recording duration
- Camera index
- Output filenames
- Proxy port
- Test domains

would be moved into configuration or command-line arguments rather than being embedded directly within the source.

---

## Error Handling

A modern implementation would provide more robust handling for:

- Missing microphones
- Missing webcams
- Device permissions
- Invalid network requests
- Connection failures
- File-writing errors
- Dependency failures
- Graceful interruption

Resources would also be managed using structured cleanup to ensure devices and files are released correctly.

---

## Testing

Individual components could be tested independently:

```text
1. Test audio capture
        |
        v
2. Test image capture
        |
        v
3. Test video capture
        |
        v
4. Test concurrent capture
        |
        v
5. Test local HTTP server
        |
        v
6. Test proxy using local web server
        |
        v
7. Verify expected request/response behaviour
```

This would make the project significantly easier to debug and reproduce.

---

# Portfolio Context

This project represents another branch of my software-development experience.

While much of my work has focused on robotics and autonomous systems, this coursework explored the underlying computer systems that modern connected devices depend upon:

```text
                     SOFTWARE ENGINEERING
                              |
          +-------------------+-------------------+
          |                                       |
          v                                       v
       Robotics                              Cybersecurity
          |                                       |
   Sensors / Control                     Networks / Protocols
          |                                       |
   Computer Vision                       HTTP / HTTPS
          |                                       |
   Autonomous Systems                    Proxy Concepts
          |                                       |
          +-------------------+-------------------+
                              |
                              v
                     Connected Systems
```

The multimedia component also overlaps with later robotics work through camera acquisition, audio I/O and concurrent sensor processing.

The project is retained as evidence of broader Python and computer-systems experience alongside my primary robotics work.
