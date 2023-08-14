package ec2

default match = false

match {
    input.MetadataOptions.HttpTokens == "optional"
}