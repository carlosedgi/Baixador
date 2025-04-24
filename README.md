
# 📥 MultiPlatform Video Downloader - `baixador.py`

Script em Python para baixar vídeos de diversas plataformas como YouTube, Twitter, Facebook, Instagram, TikTok e Reddit utilizando a poderosa biblioteca `yt-dlp`.

> Compartilhado publicamente por [@SentinelaCarioca](https://x.com/SentinelaCarioca) com o propósito de democratizar o acesso a ferramentas práticas de captura de vídeo.

---

## 🚀 Funcionalidades

- Suporte a múltiplas plataformas:
  - YouTube
  - Twitter (X)
  - Facebook
  - Instagram
  - TikTok
  - Reddit
- Salva os vídeos automaticamente em uma pasta `downloads/`
- Renomeia os vídeos com base na plataforma e no horário de download
- Suporte a cookies do navegador para Instagram (quando necessário)

---

## 🧠 Requisitos

Certifique-se de ter as bibliotecas instaladas:

```bash
pip install yt-dlp
```

Além disso, tenha o `ffmpeg` instalado e acessível no PATH do sistema (recomendado para melhor performance com `yt-dlp`).

---

## 💻 Como usar

1. Clone ou baixe este repositório.
2. Execute o script com Python:

```bash
python baixador.py
```

3. Selecione a plataforma desejada pelo menu interativo.
4. Insira o link do vídeo.
5. O vídeo será salvo automaticamente na pasta `downloads`.

---

## 📁 Estrutura de pastas

```bash
📂 downloads/
  └── YouTube_2025-04-24_15-30-00.mp4
  └── Instagram_2025-04-24_15-32-00.mp4
```

---

## 🛡️ Aviso legal

Este script é fornecido apenas para fins educacionais. O uso para baixar conteúdo protegido por direitos autorais pode violar os termos de uso das plataformas. Use com responsabilidade.

---

## ✊ Filosofia

> Informação descentralizada, acessível e distribuída.  
> Criação coletiva, conhecimento livre.  
> Por um mundo com menos amarras e mais autonomia.
