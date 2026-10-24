<div align="center">

# Chen-Yu "Enzo" Chang

**Perception and embedded systems for autonomous vehicles**

![Open to](https://img.shields.io/badge/Open_to-Summer_2027_internships-2dd4bf?style=for-the-badge&labelColor=0f172a)
![Based](https://img.shields.io/badge/Pittsburgh,_PA-CMU_MS_Civil_%26_Computer_Eng-f59e0b?style=for-the-badge&labelColor=0f172a)

</div>

| Resume and work | Projects | Contact |
|---|---|---|
| [Resume (PDF)](#) <br> [Portfolio](https://chen-yu-chang.github.io/My-Personal-Website/) | [Autonomous racecar perception](#autonomous-racecar-perception) <br> [Pedestrian intention](#pedestrian-crossing-prediction) <br> [Traffic noise monitor](#vehicle-level-traffic-noise-monitoring) | [LinkedIn](https://www.linkedin.com/in/chenyuchang0509/) <br> [Email](mailto:cchenyu.pro@gmail.com) <br> [YouTube @tenzooutoften](https://www.youtube.com/@tenzooutoften) |

---

![About](https://img.shields.io/badge/About-0f172a?style=for-the-badge&labelColor=2dd4bf)

I'm a master's student at Carnegie Mellon (Civil and Computer Engineering, graduating Dec 2027), focused on autonomous driving and smart cities. Before CMU, I spent about two and a half years at Texas Instruments as an applications engineer and product marketing engineer on automotive microcontrollers, where I benchmarked the new C29x core, validated silicon for release, and worked with OEMs and Tier 1s on next-generation requirements.

I like the place where hardware and software meet: sensors, embedded boards, and models that have to run on limited compute. I also run a Chinese-language YouTube channel on technology and industry analysis (8,000+ subscribers).

---

![Now](https://img.shields.io/badge/What_I'm_building_now-0f172a?style=for-the-badge&labelColor=f59e0b)

| Project | What it is |
|---|---|
| <a id="autonomous-racecar-perception"></a>**Autonomous racecar perception** <br> `Python` `YOLO` `SAM3` | On Carnegie Mellon Racing's perception team, I'm improving driverless cone detection with image sharpening for blue cones and previous-frame tracking to recover missed detections. I auto-labeled training data with SAM3 and Grounding DINO and trained YOLO26s. I'm now exploring model distillation to cut GPU load. |
| <a id="pedestrian-crossing-prediction"></a>**Pedestrian crossing prediction** <br> `Python` `PyTorch` | Predicting whether a pedestrian will cross 1–3 seconds early on JAAD and PIE, evaluated only on windows before the decision point to avoid label leakage. Replacing 85 raw pose keypoints with about 10 interpretable cues, fused with a GRU, and measuring each cue's added AUC. |
| <a id="vehicle-level-traffic-noise-monitoring"></a>**Vehicle-level traffic noise monitoring** <br> `ESP32` `Jetson` `CUDA` `SQL` | A low-cost roadside station that links each noise event to the vehicle that caused it. A camera model labels vehicles, and an audio-only classifier is trained on FFT features. The microphone is validated against a reference meter. |

*These are in progress. I'll add results and write-ups as they land.*

---

![Earlier](https://img.shields.io/badge/Earlier_projects-0f172a?style=for-the-badge&labelColor=2dd4bf)

| Project | What it is |
|---|---|
| **Cruise Control** <br> `C` `Node.js` | A rover that holds a stable 0.1–0.4 m/s and avoids obstacles. Fuses LiDAR, ultrasonic, and optical-encoder data with PID control tuned over live UDP and Socket.IO telemetry. |
| **BFS optimization** <br> `C` `CUDA` | Benchmarked serial, hybrid, multithreaded, and GPU breadth-first search. Reached up to 144x speedup with direction switching, cache blocking, and CUDA. |
| **Beyond Air Tapping** <br> `Swift` `Unity` `Flutter` | BU capstone for the client Rtangent. An AR pipeline that projects 3D models from a QR-coded hardware baton, with an authenticated iOS admin app. |

---

![Experience](https://img.shields.io/badge/Experience-0f172a?style=for-the-badge&labelColor=f59e0b)

**Texas Instruments**, Applications Engineer, then Product Marketing Engineer (2022–2025)
- Benchmarked C29x against C28x and competitor cores: 4.31x faster signal-chain execution. The whitepaper was nominated for Electronica Europe.
- Built a temperature-testing protocol for the F28P65x die, validating 23 units a day for product release.
- Presented an Ethernet zonal architecture with Tesla that cut wiring weight by 68%, demoed at CES 2025.
- Visited seven automotive OEMs and Tier 1s to define next-generation MCU requirements.

---

![Stack](https://img.shields.io/badge/Stack-0f172a?style=for-the-badge&labelColor=2dd4bf)

![Python](https://img.shields.io/badge/Python-0f172a?style=flat-square&logo=python&logoColor=2dd4bf)
![C++](https://img.shields.io/badge/C++-0f172a?style=flat-square&logo=cplusplus&logoColor=2dd4bf)
![CUDA](https://img.shields.io/badge/CUDA-0f172a?style=flat-square&logo=nvidia&logoColor=2dd4bf)
![PyTorch](https://img.shields.io/badge/PyTorch-0f172a?style=flat-square&logo=pytorch&logoColor=2dd4bf)
![Node.js](https://img.shields.io/badge/Node.js-0f172a?style=flat-square&logo=nodedotjs&logoColor=2dd4bf)
![Swift](https://img.shields.io/badge/Swift-0f172a?style=flat-square&logo=swift&logoColor=2dd4bf)
![Unity](https://img.shields.io/badge/Unity-0f172a?style=flat-square&logo=unity&logoColor=2dd4bf)
![AWS](https://img.shields.io/badge/AWS-0f172a?style=flat-square&logo=amazonwebservices&logoColor=2dd4bf)

`Sensor integration` · `Embedded systems` · `Computer vision` · `Machine learning` · `Autonomous vehicles`

---

![Contact](https://img.shields.io/badge/Contact-0f172a?style=for-the-badge&labelColor=f59e0b)

I'm looking for Summer 2027 internships in autonomy, perception, and embedded systems. The best way to reach me is [email](mailto:cchenyu.pro@gmail.com) or [LinkedIn](https://www.linkedin.com/in/chenyuchang0509/).

<div align="center">

`sense → model → validate → ship`

</div>
