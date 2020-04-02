# import package
import matplotlib.pyplot as plt

pop = [[31.889923,3.600523,33.333216,12.420476,40.301927,20.434176,8.199783,0.708573,150.448339,10.392226,8.078314,9.119152,4.552198,1.639131,190.010647,7.322858,14.326203,8.390505,14.131858,17.696293,33.390141,4.369038,10.238807,16.284741,1318.683096,44.22755,0.71096,64.606759,3.80061,4.133884,18.013409,4.493312,11.416987,10.228744,5.46812,0.496374,9.319622,13.75568,80.264543,6.939688,0.551201,4.906585,76.511887,5.23846,61.083916,1.454867,1.688359,82.400996,22.873338,10.70629,12.572928,9.947814,1.472041,8.502814,7.483763,6.980412,9.956108,0.301931,1110.396331,223.547,69.45357,27.499638,4.109086,6.426679,58.147733,2.780132,127.467972,6.053193,35.610177,23.301725,49.04479,2.505559,3.921278,2.012649,3.193942,6.036914,19.167654,13.327079,24.821286,12.031795,3.270065,1.250882,108.700891,2.874127,0.684736,33.757175,19.951656,47.76198,2.05508,28.90179,16.570613,4.115771,5.675356,12.894865,135.031164,4.627926,3.204897,169.270617,3.242173,6.667147,28.674757,91.077287,38.518241,10.642836,3.942491,0.798094,22.276056,8.860588,0.199579,27.601038,12.267493,10.150265,6.144562,4.553009,5.447502,2.009245,9.118773,43.997828,40.448191,20.378239,42.292929,1.133066,9.031088,7.554661,19.314747,23.174294,38.13964,65.068149,5.701579,1.056608,10.276158,71.158647,29.170398,60.776238,301.139947,3.447496,26.084662,85.262356,4.018332,22.211743,11.746035,12.311143]]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852,
            50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961,
            72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994,
            71.33800000000002, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022,
            79.483, 70.259, 56.007, 46.38800000000001, 60.916, 70.19800000000001, 82.208, 73.33800000000002, 81.757,
            64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297,
            78.623, 77.58800000000002, 71.993, 42.592, 45.678, 73.952, 59.44300000000001, 48.303, 74.241, 54.467,
            64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.90600000000001, 63.785, 79.762, 80.204,
            72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999998, 71.752, 71.421, 71.688, 75.563, 78.098,
            78.74600000000002, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.56800000000001, 79.972,
            74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000002, 74.143, 78.4,
            52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422,
            62.698, 42.38399999999999, 43.487]
# print(len(life_exp))
# Build Scatter plot
plt.scatter(pop, life_exp)
# print(len(pop))
# Show plot
plt.show()
