# AI-TrainOps 🚀  
AI-TrainOps is an automated **AI model training and optimization pipeline** using **PyTorch**, **Docker**, **GitHub Actions CI/CD**, **Prometheus & Grafana for monitoring**, and **profiling tools (perf, Valgrind, NVIDIA Nsight)**.  

## **📌 Features**
- 🏋️ **Automated AI Training Pipeline** (ResNet on CIFAR-10)
- 🐳 **Dockerized Training & Testing**
- 🚀 **CI/CD with GitHub Actions**
- 📊 **Real-time Monitoring (Prometheus & Grafana)**
- 🔍 **Performance Profiling (perf, Valgrind, NVIDIA Nsight)**
- 📂 **Logs & Artifacts for Debugging**

---

## **📌 Quick Start**
Follow these steps to **run the AI training pipeline on your machine**.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/AI-TrainOps.git
cd AI-TrainOps
```

### **2️⃣ Install Dependencies**
Ensure you have Python & Docker installed.

```bash
pip install -r requirements.txt
```

### **3️⃣ Run AI Training (Without Docker)**
```bash
python src/train.py
```
This will train a **ResNet model** on CIFAR-10 and save the model as `resnet_cifar10.pth`.

### **4️⃣ Run AI Training in Docker**
To ensure consistency, run the training inside a **Docker container**.
```bash
docker build -t ai-trainops .
docker run --rm -v $(pwd)/logs:/app/logs ai-trainops
```

### **5️⃣ Run Testing**
```bash
python src/test.py
```
This evaluates the trained model and prints accuracy.

---

## **📌 Real-Time Monitoring with Prometheus & Grafana**
Monitor AI training performance **in real time**.

### **1️⃣ Start Prometheus & Grafana**
```bash
docker-compose up -d
```

### **2️⃣ Access Dashboards**
- **Prometheus:** [`http://localhost:9090`](http://localhost:9090)
- **Grafana:** [`http://localhost:3000`](http://localhost:3000)  
  **Login:** `admin / admin`

### **3️⃣ Check Training Metrics in Prometheus**
Go to `http://localhost:9090` and query:
```
training_loss
cpu_usage_percent
memory_usage_mb
```

---

## **📌 Performance Profiling**
Optimize AI training with **perf, Valgrind, and NVIDIA Nsight**.

### **1️⃣ Profile CPU Performance (`perf`)**
```bash
docker run --rm --privileged -v $(pwd)/logs:/app/logs ai-trainops perf record -F 99 -g -- python3 src/train.py
docker run --rm --privileged -v $(pwd)/logs:/app/logs ai-trainops perf report > logs/perf_report.txt
```

### **2️⃣ Detect Memory Issues (`Valgrind`)**
```bash
docker run --rm ai-trainops valgrind --tool=memcheck --leak-check=full python3 src/train.py > logs/valgrind_report.txt
```

### **3️⃣ Analyze GPU Performance (`NVIDIA Nsight`)**
```bash
nvidia-docker run --rm ai-trainops nsight-systems-cli --target-process python3 src/train.py
```

---

## **📌 CI/CD with GitHub Actions**
The project uses **GitHub Actions** to:
✅ **Automatically Train & Test Models** on every `push`  
✅ **Cache Docker Layers to Speed Up CI/CD**  
✅ **Upload Training Logs as Artifacts for Debugging**

### **1️⃣ Trigger the CI/CD Pipeline**
Push to `main` branch:
```bash
git add .
git commit -m "Trigger CI/CD pipeline"
git push origin main
```
or manually trigger in **GitHub Actions → Run Workflow**.

### **2️⃣ View Logs in GitHub**
- Go to **GitHub → Actions**.
- Download the **training-logs.zip**.

---

## **📌 Repository Structure**
```plaintext
AI-TrainOps/
│── src/                  # Source code for AI training and optimization
│   ├── train.py          # AI model training script (ResNet on CIFAR-10)
│   ├── test.py           # Model evaluation script
│   ├── model.py          # ResNet model definition
│   ├── dataset.py        # Dataset loading utilities
│── tests/                # Unit tests for Python & C++
│── monitoring/           # Monitoring configuration (Prometheus & Grafana)
│   ├── prometheus.yml    # Prometheus scrape settings
│── logs/                 # Stores training logs
│── .github/workflows/    # CI/CD pipeline for GitHub Actions
│── docker-compose.yml    # Docker setup for monitoring
│── requirements.txt      # Python dependencies
│── Dockerfile            # Containerized environment setup
│── README.md             # Project documentation
│── .gitignore            # Ignore unnecessary files
```

---

## **📌 Contribution Guide**
Want to contribute? Follow these steps:
1. Fork the repo & clone locally.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes & commit (`git commit -m "Add new feature"`).
4. Push to GitHub (`git push origin feature-name`).
5. Open a **Pull Request**.

---

## **📌 License**
This project is licensed under the **MIT License**.

---

## **🚀 Next Steps**
- 📊 **Add More Performance Metrics to Grafana**
- 🔧 **Optimize Model with PyTorch Lightning**
- 🖥️ **Deploy as a Cloud-based AI Service**
- 🔔 **Integrate Slack/Email Alerts for Training Failures**

---

### **💡 Questions? Need Help?**
Open an **issue** or reach out! 🚀