import cv2
import numpy as np

# Screenshot der Benutzeroberfläche
image = cv2.imread("screenshot.png")  # Hier den Screenshot der UI laden

# Verwenden eines einfachen Erkennungsalgorithmus (z.B. Kantenerkennung oder Template Matching)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Template Matching für Knöpfe und Eingabefelder (du musst Vorlagenbilder von Knöpfen und Feldern erstellen)
button_template = cv2.imread("button_template.png", 0)
res = cv2.matchTemplate(edges, button_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + button_template.shape[1], pt[1] + button_template.shape[0]), (0, 0, 255), 2)

cv2.imshow('Detected UI Elements', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
