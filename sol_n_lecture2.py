# Plot KD-tree splits for the points and display a labeled figure.
import matplotlib.pyplot as plt

points = [(7,2),(5,9),(9,6),(4,7),(8,1),(7,6)]
labels = ["(7,2)","(5,9)","(9,6)","(4,7)","(8,1)","(7,6)"]

# KD-tree we chose:
# root: (7,6) split on x -> vertical line x=7 across whole plot
# left subtree (x<7): median by y -> (5,9) splits with horizontal line y=9 for x in [3.5,7)
#   left child: (4,7)
# right subtree (x>=7 except root): median by y -> (7,2) splits with horizontal line y=2 for x in [7,9.5]
#   left: (8,1), right: (9,6)

xmin, xmax = 3.5, 9.5
ymin, ymax = 0.0, 10.0

fig, ax = plt.subplots(figsize=(6,6))
# scatter points and annotate
for (x,y),lab in zip(points, labels):
    ax.scatter(x,y)
    ax.annotate(lab, (x+0.08, y+0.08))

# root vertical split at x=7
ax.plot([7,7],[ymin,ymax], linestyle='--')

# left subtree horizontal split y=9, limited to left region (xmin..7)
ax.plot([xmin,7],[9,9], linestyle='--')

# right subtree horizontal split y=2, limited to right region (7..xmax)
ax.plot([7,xmax],[2,2], linestyle='--')

# annotate nodes in tree positions (draw small boxes)
ax.text(7.05,6.05, "root\n(7,6)\nsplit x", fontsize=9)
ax.text(4.2,9.05, "(5,9)\nsplit y", fontsize=8)
ax.text(7.05,2.05, "(7,2)\nsplit y", fontsize=8)

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("KD-tree splits (root x, then y, then x...)")
ax.set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
