# Mission 7 — How Computers Communicate

## 1. Task / objective
The objective of this mission is to understand how computer networks connect devices to transmit data and share resources. This involves explaining eight fundamental networking concepts and architectures, observing real network diagnostics on macOS using `ping` and `nslookup`, analyzing latency and DNS resolution for a public web domain (`example.com`), and detailing the step-by-step technical lifecycle of what happens when a web page is requested in a browser.

## 2. Work completed
- Explored and documented eight essential networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server) with real-world examples.
- Conducted an ICMP connectivity test to `example.com` via `ping -c 4`, recording packet transmission, zero packet loss, and round-trip latency statistics.
- Performed a DNS name lookup on `example.com` using `nslookup`, analyzing returned A records and name server mappings.
- Wrote a 7-step explanation of what occurs when a user enters a URL in a web browser, correctly incorporating the terms *client*, *server*, *DNS*, *router*, and *protocol*.
- Redacted all sensitive local network identifiers (local IP addresses, default gateway MACs, and Wi-Fi SSID) to ensure privacy safety.

## 3. Commands / tools used
- `ping -c 4 example.com`: Transmits four ICMP Echo Request packets to a target host to test reachability, network latency, and packet loss.
- `nslookup example.com`: Queries Domain Name System (DNS) servers to resolve a domain name into its corresponding IP addresses.
- macOS Network Stack: The kernel networking subsystem managing socket connections and TCP/IP routing.

## 4. My understanding

### Task 7.1 — Network Concepts Table

| Concept | Explain It In Your Own Words | Practical Example |
|:---|:---|:---|
| **LAN (Local Area Network)** | A high-speed network that interconnects computers and devices within a limited physical area, such as a single home, classroom, or office building. | The Wi-Fi network in my house connecting my laptop, printer, and smart TV. |
| **MAN (Metropolitan Area Network)** | A network that spans a larger geographical area than a LAN, such as an entire university campus, municipality, or city. | A city-wide fiber optic network connecting municipal government offices, hospitals, and traffic control centers. |
| **WAN (Wide Area Network)** | A telecommunications network spanning large geographical areas across cities, countries, or globally. | The global Internet, which interconnects millions of independent private and public networks. |
| **DNS (Domain Name System)** | The internet's distributed directory service that translates human-readable domain names into machine-readable IP addresses. | Translating the human name `example.com` into the routing IP address `172.66.147.243`. |
| **Router** | A specialized networking hardware device that directs data packets between different networks based on destination IP routing tables. | A home Wi-Fi gateway routing data between devices on the private LAN and the public Internet Service Provider (ISP). |
| **Protocol** | A standardized, formal set of rules and conventions that govern how devices format, transmit, and receive data across a network. | **HTTP / HTTPS** for transferring hypermedia documents on the web, or **TCP** for reliable, ordered stream delivery. |
| **Packet Switching** | A communication method where digital data is partitioned into small, addressed chunks called packets that travel independently along optimal paths before being reassembled at the destination. | Streaming a video where chunks of audio and video data travel across various internet routes and reassemble seamlessly in the media player. |
| **Client-Server Architecture** | A computing structure where a client device initiates requests for services or resources, and a centralized server processes the requests and returns responses. | A web browser (client) requesting an HTML web page from an Apache or Nginx web server (server). |

---

### Task 7.2 — Observing Network Information

#### 1. Connectivity Test (`ping -c 4 example.com`)
```text
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=54 time=66.986 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=54 time=67.420 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=54 time=57.518 ms
64 bytes from 172.66.147.243: icmp_seq=3 ttl=54 time=107.081 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 57.518/74.751/107.081/19.080 ms
```

#### 2. DNS Lookup (`nslookup example.com`)
```text
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

#### Analysis Questions:
- **What does a connectivity test help you check?**  
  A `ping` test checks whether an end-to-end communication path exists between your local computer and a remote host. It measures packet loss percentage (indicating network reliability or congestion) and round-trip time (RTT latency in milliseconds), indicating how fast data travels back and forth.
- **What information does a DNS lookup display?**  
  `nslookup` displays which DNS resolver server handled the query (e.g., Google Public DNS `8.8.8.8` on UDP port `53`), whether the answer was authoritative or cached (non-authoritative), and the specific IPv4/IPv6 addresses mapped to the requested domain name (`172.66.147.243` and `104.20.23.154`).
- **What is the role of DNS when you enter a website name in a browser?**  
  Routers and network switches cannot interpret human names like `google.com` or `example.com`; they can only route packets based on numerical IP addresses. DNS acts as an automated phonebook, translating the domain name typed by the user into the destination IP address so the browser can contact the server.

---

### Task 7.3 — What Happens When You Open a Website? (7-Step Lifecycle)

1. **Step 1: User Request & Local Cache Inspection**  
   The user enters a URL (e.g., `https://example.com`) into the web browser (**client**). The browser checks its internal DNS cache and the operating system cache to see if the IP address for `example.com` was recently resolved.
2. **Step 2: DNS Resolution**  
   If the IP address is not cached locally, the client sends a **DNS** query through the local network to a recursive DNS resolver (such as `8.8.8.8`). The DNS hierarchy resolves the domain name into an IP address (`172.66.147.243`) and returns it to the client.
3. **Step 3: Network Routing**  
   The client creates an initial network connection packet. The local Wi-Fi **router** inspects the packet header and forwards it across external ISP gateway routers via packet switching until it arrives at the target **server** across the WAN.
4. **Step 4: TCP Handshake & TLS Encryption (Protocols)**  
   The client and server establish a reliable connection using the Transmission Control **Protocol** (TCP 3-way handshake: SYN, SYN-ACK, ACK). If using HTTPS, a Transport Layer Security (TLS) cryptographic handshake follows to negotiate encryption keys for secure communication.
5. **Step 5: Sending the HTTP GET Request**  
   The browser sends an HTTP GET request **protocol** message across the encrypted channel asking the web server for the root web document (`/`).
6. **Step 6: Server Processing & Response Generation**  
   The web **server** receives the request, processes it, retrieves the requested HTML document, and transmits back an HTTP response packet with a status code (e.g., `200 OK`) and the payload (HTML, CSS, assets).
7. **Step 7: Client Parsing & DOM Rendering**  
   The browser receives the response packets, reassembles them, parses the HTML, builds the Document Object Model (DOM), loads linked CSS and JavaScript assets, and renders the visual web page on the user's screen.

---

## 5. Difficulties faced
When looking at `nslookup` output, two distinct IP addresses (`172.66.147.243` and `104.20.23.154`) were returned for the exact same domain name.

## 6. How I resolved them
I researched multi-IP DNS answers and discovered that popular websites use Anycast routing and Content Delivery Networks (CDNs) with multiple server IP addresses for load balancing and redundancy, so DNS can return multiple valid server addresses.

## 7. Evidence / files
- Mission documentation: `mission-07-networking/README.md`
- Network concepts table (Task 7.1)
- Live `ping` latency output (0.0% packet loss, 74.7 ms avg RTT)
- Live `nslookup` domain resolution output
- 7-step website opening lifecycle (Task 7.3)

## 8. Commit details
- **Commit message**: `Explain networking concepts and website communication`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
