import cv2
import numpy as np

# Hauptbild zum erkennen
hustle_png = cv2.imread('hustle.png', cv2.IMREAD_UNCHANGED)
# bild was im bild erkannt werden soll!
geld_png = cv2.imread('geld.png', cv2.IMREAD_UNCHANGED)

# ruft das Hauptbild auf
cv2.imshow('Hustle', hustle_png)
cv2.waitKey()
cv2.destroyAllWindows()

# ruft das gesuchte bild auf
cv2.imshow('Geld', geld_png)
cv2.waitKey()
cv2.destroyAllWindows()

# unterschiedliche Algorythemn testen um das beste ergebnis zu bekommen!
#  Bild indem gesucht wird== bauenhof_png | bild nachdem gesucht wird im bild
ergebnis = cv2.matchTemplate(hustle_png, geld_png, cv2.TM_CCOEFF_NORMED)

# zeigt das ergebnis an
cv2.imshow('Ergebnis', ergebnis)
cv2.waitKey()
cv2.destroyAllWindows()
min_wert, max_wert, min_ort, max_ort = cv2.minMaxLoc(ergebnis)

# bereicht nachdem das bild gesucht werden soll
max_ort = (671, 807)  # Wenn du max_ort manuell festlegst
max_wert = (0.9999998927116394)
breite = geld_png.shape[1]
höhe = geld_png.shape[0]

# Zeichnet das Rechteck
cv2.rectangle(hustle_png, max_ort, (max_ort[0] + breite, max_ort[1] + höhe), (0, 255, 255), 2)
# Zeigt das geänderte Bild an
cv2.imshow('Ergebnis mit Rechteck', hustle_png)
cv2.waitKey(0)
cv2.destroyAllWindows()