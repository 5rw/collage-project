#include <botan/auto_rng.h>
#include <botan/dilithium.h>
#include <botan/hex.h>
#include <iostream>
#include <string>

int main() {
    try {
        // Initialize Botan
        Botan::LibraryInitializer init;

        // Create a random number generator
        Botan::AutoSeeded_RNG rng;

        // Generate Dilithium key pair
        Botan::Dilithium_PrivateKey private_key(rng, 3); // 3 corresponds to Dilithium3 parameter set
        Botan::Dilithium_PublicKey public_key = private_key;

        // Message to sign
        std::string message = "Hello, Quantum-Secure World!";
        std::vector<uint8_t> message_bytes(message.begin(), message.end());

        // Sign the message
        Botan::PK_Signer signer(private_key, rng, "Dilithium");
        std::vector<uint8_t> signature = signer.sign_message(message_bytes, rng);

        std::cout << "Signature: " << Botan::hex_encode(signature) << std::endl;

        // Verify the signature
        Botan::PK_Verifier verifier(public_key, "Dilithium");
        bool valid = verifier.verify_message(message_bytes, signature);

        if (valid) {
            std::cout << "Signature verification successful!" << std::endl;
        } else {
            std::cout << "Signature verification failed!" << std::endl;
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}