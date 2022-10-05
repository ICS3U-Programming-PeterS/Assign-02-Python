#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Oct 3, 2022
# This program calculates the lateral surface, surface area and volume of a truncated elliptic cone


# imports
import math

# functions

# function that calculates volume and prints it
def volume(
    cone_height,
    smajor_axis_base,
    sminor_axis_base,
    cutoff_height,
    smajor_axis_top,
    sminor_axis_top,
):
    tec_volume = (
        math.pi
        / 3
        * (
            cone_height * smajor_axis_base * sminor_axis_base
            - cutoff_height * smajor_axis_top * sminor_axis_top
        )
    )
    print(
        "\nThe volume of the truncated elliptic cone is: {:.2f} cm^3".format(tec_volume)
    )


# function that calculates lateral surface and prints it
def lateral_surface(
    cone_height,
    smajor_axis_base,
    sminor_axis_base,
    cutoff_height,
    smajor_axis_top,
    sminor_axis_top,
):
    lateral_surface = (
        1
        / 2
        * math.pi
        * (
            (
                smajor_axis_base * math.sqrt(sminor_axis_base**2 + cone_height**2)
                + sminor_axis_base * math.sqrt(smajor_axis_base**2 + cone_height**2)
            )
            - (
                smajor_axis_top * math.sqrt(sminor_axis_top**2 + cutoff_height**2)
                + sminor_axis_top * math.sqrt(smajor_axis_top**2 + cutoff_height**2)
            )
        )
    )
    print(
        "The lateral surface of the truncated elliptic cone is: {:.2f} cm^2".format(
            lateral_surface
        )
    )


# function that calculates surface area and prints it
def surface_area(
    cone_height,
    smajor_axis_base,
    sminor_axis_base,
    cutoff_height,
    smajor_axis_top,
    sminor_axis_top,
):
    tec_surface_area = 1 / 2 * math.pi * (
        (
            smajor_axis_base * math.sqrt(sminor_axis_base**2 + cone_height**2)
            + sminor_axis_base * math.sqrt(smajor_axis_base**2 + cone_height**2)
        )
        - (
            smajor_axis_top * math.sqrt(sminor_axis_top**2 + cutoff_height**2)
            + sminor_axis_top * math.sqrt(smajor_axis_top**2 + cutoff_height**2)
        )
    ) + math.pi * (
        smajor_axis_base * sminor_axis_base + smajor_axis_top * sminor_axis_top
    )
    print(
        "The surface area of the truncated elliptic cone is: {:.2f} cm^2".format(
            tec_surface_area
        )
    )


def main():
    # if statement to choose whether to solve for Surface area(sa) or Volume(v)
    sa_or_v = input("What do you want to solve for Surface area (sa) or Volume (v): ")
    if sa_or_v == "v":
        # this gets the input for all needed values
        cone_height = float(input("What is the cone height(cm): "))
        smajor_axis_base = float(input("What is the semi-major axis base(cm): "))
        sminor_axis_base = float(input("What is the semi-minor axis base(cm): "))
        cutoff_height = float(input("What is the cutoff height(cm): "))
        smajor_axis_top = float(input("What is the semi-major axis top(cm): "))
        sminor_axis_top = float(input("What is the semi-minor axis top(cm): "))
        # calling the functions
        volume(
            cone_height,
            smajor_axis_base,
            sminor_axis_base,
            cutoff_height,
            smajor_axis_top,
            sminor_axis_top,
        )
        lateral_surface(
            cone_height,
            smajor_axis_base,
            sminor_axis_base,
            cutoff_height,
            smajor_axis_top,
            sminor_axis_top,
        )
        surface_area(
            cone_height,
            smajor_axis_base,
            sminor_axis_base,
            cutoff_height,
            smajor_axis_top,
            sminor_axis_top,
        )

    else:
        # this gets the input for all needed values
        cone_height = float(input("What is the cone height(cm): "))
        smajor_axis_base = float(input("What is the semi-major axis base(cm): "))
        sminor_axis_base = float(input("What is the semi-minor axis base(cm): "))
        cutoff_height = float(input("What is the cutoff height(cm): "))
        smajor_axis_top = float(input("What is the semi-major axis top(cm): "))
        sminor_axis_top = float(input("What is the semi-minor axis top(cm): "))
        print("")
        # calling the functions
        lateral_surface(
            cone_height,
            smajor_axis_base,
            sminor_axis_base,
            cutoff_height,
            smajor_axis_top,
            sminor_axis_top,
        )
        surface_area(
            cone_height,
            smajor_axis_base,
            sminor_axis_base,
            cutoff_height,
            smajor_axis_top,
            sminor_axis_top,
        )


if __name__ == "__main__":
    main()
