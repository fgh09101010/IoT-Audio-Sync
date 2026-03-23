# IoT-Audio-Sync: MQTT 智慧音樂播放裝置

[https://youtu.be/tAb-IGLaYkQ](https://youtu.be/tAb-IGLaYkQ)

## 專案簡介
這是一個基於物聯網（IoT）技術的遠端音樂控制與播放系統。透過 Node-RED 介面，使用者可以遠端調整播放參數並選擇歌曲，系統會透過 MQTT 協定將指令傳送至 ESP32 硬體終端，驅動蜂鳴器播放音樂，同時結合 LED 燈條與 OLED 顯示器提供視覺回饋。

## 主要功能
* **遠端音樂控制**：透過 Node-RED Dashboard 介面，可即時調整 `Duty`（占空比/音量）並選擇欲播放的歌曲。
* **即時通訊**：使用 MQTT 協定（broker.mqttgo.io）進行軟硬體間的低延遲訊息傳輸。
* **多維度視覺回饋**：
    * **OLED 顯示器**：顯示當前曲目名稱、播放剩餘時間及頻率進度條。
    * **WS2812B LED 燈條**：燈光色彩與排列會隨音調（頻率）高低即時變換。
    * **7 段顯示器**：提供精確的播放倒數計時。
* **資料庫整合**：系統會自動從 MySQL 資料庫讀取歌曲頻率數據，實現靈活的曲庫管理。
* **手動中止功能**：硬體端設有實體按鈕，可隨時強制中斷當前播放任務。

## 系統架構

## 硬體設備 (Bill of Materials)
* **ESP32**：核心控制開發板。
* **Buzzer**：負責音樂播放。
* **WS2812B RGB LED**：8 燈位全彩燈條。
* **OLED (SSD1306)**：128x64 圖像化資訊顯示。
* **TM1637**：4 位數 7 段顯示計時器。
* **Push Button**：緊急停止開關。

## 軟體技術棧
* **韌體**：MicroPython (負責 I2C/PWM 控制、MQTT 訂閱、多執行緒處理)。
* **後端控制**：Node-RED (Dashboard 製作、MQTT 發送、MySQL 查詢)。
* **通訊協定**：MQTT (Quality of Service: QoS 0/1)。
* **資料庫**：MySQL (儲存歌曲名稱與頻率陣列)。

## 快速開始
1. **資料庫部署**：匯入 `music_database.sql`，建立歌曲頻率對應表。
2. **Node-RED 配置**：匯入 `flows.json`，並確保 MQTT 節點指向正確的 Topic。
3. **燒錄韌體**：將 `main.py` 與相關驅動模組上傳至 ESP32。
4. **運行**：開啟 Node-RED 控制介面，選擇歌曲並點擊「確認」即可播放。

## 成果展示
詳細的軟體操作與硬體運作展示，請觀看我們的[專題展示影片](https://youtu.be/tAb-IGLaYkQ)。


