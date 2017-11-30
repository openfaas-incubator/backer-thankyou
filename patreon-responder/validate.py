import hmac

def validate_hmac(sender_digest, key, body):
    digest_maker = hmac.new(key)
    digest_maker.update(body)
    digest = digest_maker.hexdigest()

    print("Digests", sender_digest, digest, str(sender_digest) == str(digest))

    return str(sender_digest) == str(digest)

#with open("README.md", "r") as f:    
#    validate_hmac("b61f0203ba1ba256c48eb66d1597aa51", "my-secret", f.read())

