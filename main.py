import pydicom
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

plt.plot(x, y)
plt.title("Графічний примітив: Коло")
plt.axis('equal')
plt.show()

# Завантаження та відображення DICOM-файлу
dicom_file = 'test1.dcm'
ds = pydicom.dcmread(dicom_file)

# Отримання піксельних даних та їх візуалізація
plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
plt.title(f"Медичне зображення DICOM: {ds.PatientName}")
plt.show()
