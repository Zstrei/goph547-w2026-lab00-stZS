import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from goph547lab00.arrays import (
    square_ones,
)

def arrays():

    A_np = np.ones((3, 3))
    A = square_ones(3)
    print(f"A_np:\n{A_np}")
    print(f"A:\n{A}")
    print()

    # Question B1
    C = np.ones((3, 5))
    print(f"Question B1: (3, 5) array of ones\n{C}")

   # Question B2 
    D = np.full((6, 3), np.nan)
    print(f"Question B2: (6, 3) array of nans\n{D}")
    print()

    # Question B3
    odd_col = np.arange(45, 75, 2).reshape(-1, 1)
    print("Question B3: Column vector of odd numbers between 44 and 75")
    print(odd_col)
    print()

    # Quwstion B4 
    total = np.sum(odd_col)
    print("Question B4: Sum of all numbers printed in Question B3")
    print(total)

    # Question B5 
    A = np.array([
        [5,  7,  2],
        [1, -2,  3],
        [4,  4,  4]
    ])
    print("Question B5: Specified 3x3 array")
    print(A)
    print()

    #Question B6
    B = np.eye(3)
    print("Question B6: 3x3 identity matrix")
    print(B)
    print()

    #Question B7
    C = A * B
    print("Question B7: Element-wise multiplication of A and B")
    print(C)
    print()

    # Question B8
    D = np.matmul(A,B)
    print("Question B8: Matrix multiplication (dot product) of A and B")
    print(D)
    print()

    # Question B9
    E = np.cross(A, B)
    print("Question B9: Cross product of A and B (row-wise)")
    print(E)
    print()

    # Question B10
    img_array = np.asarray(Image.open('rock_canyon.jpg'))
    print("Question B10: Loaded rock_canyon image")
    print(f"Image shape: {img_array.shape}")
    print()

    # Question B11: plots image using imshow() fucntion
    img_plot = plt.imshow(img_array)
    plt.show()
    print(f'Question B11. Shape:\n{img_array.shape}')
    print()

    # Question B12
    gray_img = np.asarray(Image.open("rock_canyon.jpg").convert("L"))
    print("Question B12: Grayscale image loaded with PIL")
    print(f"Grayscale image shape: {gray_img.shape}")
    print()

    # Question B13
    smaller_img = gray_img[168:233, 119:147]
    print(f'Question B13. Smaller image shape Shape:\n{smaller_img.shape}')
    plt.figure()
    plt.imshow(smaller_img, cmap='gray')
    plt.title("Small_Grey_Image")
    plt.axis('off')
    plt.show()
    print()

   # Question B14 and B15

    # Separate color channels
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]

    # ---- Plot (i): mean along y-direction vs x-coordinate ----
    mean_R_x = np.mean(R, axis=0)
    mean_G_x = np.mean(G, axis=0)
    mean_B_x = np.mean(B, axis=0)
    mean_RGB_x = np.mean(img_array, axis=(0, 2))

    # ---- Plot (ii): mean along x-direction vs y-coordinate ----
    mean_R_y = np.mean(R, axis=1)
    mean_G_y = np.mean(G, axis=1)
    mean_B_y = np.mean(B, axis=1)
    mean_RGB_y = np.mean(img_array, axis=(1, 2))

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot (i)
    axes[0].plot(mean_R_x, color="red", label="Mean R")
    axes[0].plot(mean_G_x, color="green", label="Mean G")
    axes[0].plot(mean_B_x, color="blue", label="Mean B")
    axes[0].plot(mean_RGB_x, color="black", linewidth=2, label="Mean RGB")
    axes[0].set_xlabel("x-coordinate")
    axes[0].set_ylabel("Colour value")
    axes[0].set_title("Mean colour values vs x-coordinate")
    axes[0].legend()

    # Plot (ii)
    axes[1].plot(mean_R_y, np.arange(len(mean_R_y)), color="red", label="Mean R")
    axes[1].plot(mean_G_y, np.arange(len(mean_G_y)), color="green", label="Mean G")
    axes[1].plot(mean_B_y, np.arange(len(mean_B_y)), color="blue", label="Mean B")
    axes[1].plot(mean_RGB_y, np.arange(len(mean_RGB_y)), color="black", linewidth=2, label="Mean RGB")
    axes[1].set_xlabel("Colour value")
    axes[1].set_ylabel("y-coordinate")
    axes[1].set_title("Mean colour values vs y-coordinate")
    axes[1].legend()

    plt.tight_layout()
    plt.show()
    print("Question 14 and 15: Plots created succesfully")
    print()

    #Question B16
    plt.tight_layout()
    plt.savefig("rock_canyon_RGB_summary.png")
    print('Question 16: Saved RGB summary image in examples folder')


if __name__ == '__main__':
    arrays()