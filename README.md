# Analiza e Dallimeve në Kohë Përgjigje dhe Menaxhimin e Resurseve  
## Mjetet Lokale (Grid) vs. Google Cloud Monitoring (Cloud)

---

### 📊 Matjet, Qëllimi dhe Metodologjia

Qëllimi i këtyre matjeve është të analizohet performanca e një serveri Python Flask në ambient cloud (Google Cloud VM) dhe të krahasohet me matjet manuale të realizuara përmes mjeteve lokale.

**Mjetet e përdorura:**

- **Google Cloud Platform (GCP)**  
  Përdoret për vendosjen dhe testimin e shërbimeve cloud.
  
- **Google Cloud Monitoring**  
  Për monitorim të përdorimit të:
  - CPU-së
  - RAM-it
  - Rrjetit
  - Diskut  
  në kohë reale.
  
- **Mjete Lokale:**
  - `top` dhe `htop` për përdorimin e CPU dhe RAM
  - `curl` për testimin e HTTP dhe matjen e kohës së përgjigjes
  - `time python3 server.py` për matjen e kohës së ekzekutimit të serverit

---

### 🖥️ Analiza e Performancës përmes Matjeve Lokale  
**(GRID, curl, time, top dhe htop)**

Ky skript Python është krijuar për të testuar performancën e një aplikacioni web duke simuluar ngarkesë me kërkesa HTTP paralele në një URL të caktuar.

**Karakteristikat:**

- Përdoren procese të shumëfishta për të simuluar përdorues të ndryshëm.
- Kërkesat shpërndahen në mënyrë të barabartë (qasje Grid).
- Matje të:
  - Kohës së përgjigjes
  - Numrit të kërkesave
  - Dështimeve
  - Burimeve sistemore:
    - CPU (%)
    - RAM (MB)
    - Trafiku i rrjetit (MB)

📁 Rezultatet ruhen në një file `.csv` për analizë të mëvonshme.

---

### ☁️ Matjet në Google Cloud Platform përmes **Cloud Monitoring**

**Google Cloud Monitoring** është një mjet i fuqishëm për monitorim të resurseve në kohë reale në ambient cloud.

**Përfitimet dhe funksionet:**

- Mbledhje, vizualizim dhe analizë e metrikeve kritike të sistemit.
- Monitorim i:
  - Përdorimit të CPU-së
  - RAM-it
  - Rrjetit
  - Diskut
- Ndihmon në menaxhimin efikas të infrastrukturës cloud.
- Analizë e performancës dhe e përdorimit të resurseve në mënyrë të centralizuar dhe të automatizuar.

---

> Kjo analizë ofron një krahasim praktik dhe të detajuar mes qasjes tradicionale të matjeve përmes mjeteve lokale dhe potencialit të monitorimit modern të cloud-it përmes Google Cloud Platform.
