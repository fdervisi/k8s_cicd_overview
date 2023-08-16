package ec2

default match = false

# Check if an instance's associated role has the AmazonSSMManagedInstanceCore managed policy
match {
    some i
    input.Role.Policies[i] == "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}
