<!DOCTYPE html>
<html lang="sq">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Analiza e Performancës: Lokale vs Cloud</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f8f9fa;
      margin: 0;
      padding: 20px;
      color: #333;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    h1, h2 {
      color: #0a66c2;
    }
    h1 {
      border-bottom: 2px solid #0a66c2;
      padding-bottom: 10px;
    }
    ul {
      line-height: 1.6;
    }
    .section {
      margin-bottom: 30px;
    }
    code {
      background-color: #f1f1f1;
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 90%;
    }
    .highlight {
      background-color: #e9f5ff;
      padding: 10px;
      border-left: 4px solid #0a66c2;
      margin: 20px 0;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Analiza e Dallimeve në Kohë Përgjigje dhe Menaxhimin e Resurseve:</h1>
    <h2>Mjetet Lokale (Grid) vs. Google Cloud Monitoring (Cloud)</h2>

    <div class="section">
      <h3>Matjet, Qëllimi dhe Metodologjia</h3>
      <p>Qëllimi i këtyre matjeve është të analizohet performanca e një serveri Python Flask në ambient cloud (Google Cloud VM) dhe të krahasohet me matjet manuale të realizuara përmes mjeteve lokale.</p>

      <div class="highlight">
        <strong>Mjete të përdorura:</strong>
        <ul>
          <li><strong>Google Cloud Platform (GCP):</strong> për vendosjen dhe testimin e shërbimeve cloud</li>
          <li><strong>Google Cloud Monitoring:</strong> për monitorim të CPU, RAM, rrjetit dhe diskut në kohë reale</li>
          <li><strong>Mjete Lokale:</strong>
            <ul>
              <li><code>top</code> dhe <code>htop</code> për CPU dhe RAM</li>
              <li><code>curl</code> për testimin e HTTP</li>
              <li><code>time python3 server.py</code> për kohën e ekzekutimit</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <div class="section">
      <h3>Analiza Lokale e Performancës (GRID, curl, time, top, htop)</h3>
      <p>Skript Python është ndërtuar për të testuar performancën e një aplikacioni web duke simuluar ngarkesë me kërkesa HTTP paralele në një URL të caktuar.</p>

      <ul>
        <li>Përdorimi i proceseve të shumëfishta për simulim të përdoruesve</li>
        <li>Matje të:
          <ul>
            <li>Kohës së përgjigjes</li>
            <li>Numrit të kërkesave</li>
            <li>Dështimeve</li>
            <li>Burimeve sistemore:
              <ul>
                <li>CPU (%)</li>
                <li>RAM (MB)</li>
                <li>Trafiku i rrjetit (MB)</li>
              </ul>
            </li>
          </ul>
        </li>
        <li>Rezultatet ruhen në file <code>.csv</code> për analizë të mëvonshme</li>
      </ul>
    </div>

    <div class="section">
      <h3>Matjet në Google Cloud Platform (Cloud Monitoring)</h3>
      <p>Google Cloud Platform (GCP) ofron një mjet të fuqishëm për monitorim të resurseve në kohë reale – <strong>Cloud Monitoring</strong>.</p>

      <ul>
        <li>Lejon zhvilluesit dhe administratorët të:
          <ul>
            <li>Mblidhen metrika të sistemit</li>
            <li>Vizualizojnë përdorimin e CPU, RAM, rrjetit dhe diskut</li>
            <li>Menaxhojnë efikasitetin e resurseve në ambientin cloud</li>
          </ul>
        </li>
        <li>Ndihmon në identifikimin e pikave kritike në performancë</li>
      </ul>
    </div>
  </div>
</body>
</html>
