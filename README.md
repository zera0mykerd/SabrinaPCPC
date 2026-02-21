# SabrinaPCPC — Documentazione Tecnica

## Panoramica

SabrinaPCPC è un'applicazione desktop professionale per Linux con interfaccia grafica Tkinter.
Offre due funzionalità principali:

1. **Compressione File Multimediali** — Immagini (JPG, PNG) e video (MP4, MOV)
2. **Confronto Avanzato Cartelle** — Verifica integrità e corrispondenza backup

---

## Requisiti di sistema

- Sistema operativo: **Linux** (Ubuntu 20.04+, Debian, Fedora, Arch)
- Python: **3.10+**
- Tkinter incluso nella distribuzione Python standard

---

## Installazione dipendenze Python

```bash
pip install Pillow av-python opencv-python-headless pyinstaller
```

### Dipendenze dettagliate

| Libreria | Versione | Uso | Obbligatoria |
|---|---|---|---|
| Pillow | ≥9.0 | Compressione JPG/PNG | ✅ Sì |
| av (PyAV) | ≥10.0 | Compressione video H.264 | Consigliata |
| opencv-python-headless | ≥4.7 | Fallback compressione video | Opzionale |
| pyinstaller | ≥5.0 | Build eseguibile | Solo per distribuzione |

> **Nota**: Se né PyAV né OpenCV sono installati, la compressione video viene saltata
> con avviso nel log. Le immagini vengono sempre elaborate se Pillow è presente.

---

## Avvio in sviluppo

```bash
python SabrinaPCPC.py
```

---

## Build eseguibile (--onefile)

```bash
# Metodo 1: usando il file .spec
pyinstaller SabrinaPCPC.spec

# Metodo 2: comando diretto
pyinstaller --onefile --windowed \
  --hidden-import PIL \
  --hidden-import PIL.Image \
  --hidden-import PIL.JpegImagePlugin \
  --hidden-import PIL.PngImagePlugin \
  --hidden-import av \
  --hidden-import cv2 \
  --name SabrinaPCPC \
  SabrinaPCPC.py
```

L'eseguibile finale sarà in `dist/SabrinaPCPC`.

---

## Architettura del codice

```
SabrinaPCPC.py
├── COLORS / FONTS          ← Palette e tipografia
├── CompressoreImmagini     ← Logica compressione JPG/PNG (Pillow)
├── CompressoreVideo        ← Logica compressione MP4/MOV (PyAV/OpenCV)
├── AnalizzatoreCartelle    ← Logica confronto e integrità
├── BottoneBello            ← Widget bottone arrotondato custom
├── BarraProgresso          ← Widget barra progresso custom
├── LogArea                 ← Widget area log colorata
├── SchermataBase           ← Classe base schermate
├── SchermataHome           ← Schermata principale
├── SchermataCompressione   ← Funzione 1
├── SchermataConfronto      ← Funzione 2
└── App                     ← Controller principale Tkinter
```

---

## Funzione 1 — Compressione

### File supportati
- `.jpg`, `.jpeg` → Compressione JPEG ottimizzata (qualità regolabile 50-95%)
- `.png` → Conversione in JPG + compressione (PNG originale eliminato solo se successo)
- `.mp4`, `.mov` → Compressione H.264 con CRF 26 (PyAV) o MP4V (OpenCV fallback)

### Sicurezza
- Backup temporaneo del file originale prima di ogni operazione
- In caso di errore: ripristino automatico, file originale intatto
- Se il file compresso è più grande dell'originale: viene mantenuto l'originale

---

## Funzione 2 — Confronto Cartelle

### Analisi eseguite
1. **Struttura**: file mancanti, file extra, percorsi diversi
2. **Dimensioni**: confronto byte per byte senza lettura contenuto
3. **Hash SHA256**: confronto contenuto in streaming (memoria efficiente)
4. **Integrità**: verifica apertura immagini (Pillow) e lettura frame video (PyAV/OpenCV)

### Garanzie
- **NESSUN file viene modificato, spostato o eliminato**
- Solo lettura + analisi + report

### Export
- `.txt` — report leggibile formattato
- `.csv` — dati strutturati per analisi in spreadsheet

---

## Thread safety

Tutte le operazioni lunghe vengono eseguite in thread separati (daemon thread).
La GUI rimane sempre reattiva. L'utente può interrompere qualsiasi operazione
tramite il pulsante "Interrompi" (threading.Event).

---

## Palette colori

| Nome | Hex | Uso |
|---|---|---|
| Bianco caldo | `#FDF6F0` | Sfondo principale |
| Rosa cipria | `#FAF0F5` | Pannelli header |
| Lilla medio | `#C9A0C0` | Accento primario, bottoni |
| Viola profondo | `#9B72A0` | Hover, accenti forti |
| Rosa cipria med. | `#E8B4CB` | Accenti secondari |

---

## Risoluzione problemi

**Il programma non si avvia:**
```bash
python -c "import tkinter; tkinter.Tk().mainloop()"
# Se fallisce: sudo apt install python3-tk
```

**Pillow non trovato:**
```bash
pip install Pillow --upgrade
```

**Video non compresso:**
```bash
pip install av
# oppure
pip install opencv-python-headless
```

---

*SabrinaPCPC v1.0 — Software professionale per Linux*
