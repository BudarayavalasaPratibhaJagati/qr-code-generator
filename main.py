import argparse, os, time
import qrcode

def make_qr(url: str, out_dir: str = "qr_codes"):
    os.makedirs(out_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(out_dir, f"qr_{ts}.png")
    img = qrcode.make(url)
    img.save(path)
    print(f"[OK] Saved QR to {path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True, help="URL to encode as QR")
    args = p.parse_args()
    make_qr(args.url)

