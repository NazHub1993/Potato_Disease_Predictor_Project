import React, { useState } from "react";

const Home = () => {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file));
            setResult(null);
        }
    };

    const handleSubmit = async () => {
        if (!image) return;

        const formData = new FormData();
        formData.append("file", image);

        setLoading(true);

        try {
            const response = await fetch("http://localhost:8000/predict", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            setResult(data);
        } catch (error) {
            console.error("Error:", error);
            alert("Failed to connect to the server.");
        }

        setLoading(false);
    };
    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-100 to-green-300 p-4 font-sans">
            {/* Container (Replaces Card) */}
            <div className="w-full max-w-md bg-white shadow-2xl rounded-2xl border border-green-200 p-6 space-y-5">

                <h1 className="text-2xl font-bold text-center text-green-800">
                    Potato Disease Predictor 🌿
                </h1>

                {/* Upload Area */}
                <label className="flex flex-col items-center justify-center border-2 border-dashed border-green-400 rounded-xl p-6 cursor-pointer hover:bg-green-50 transition">
                    {/* Simple SVG icon replacement for UploadCloud */}
                    <svg className="w-10 h-10 text-green-600 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                    </svg>
                    <span className="text-green-700 font-medium">
                        Click to upload leaf image
                    </span>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={handleImageChange}
                        className="hidden"
                    />
                </label>

                {/* Preview */}
                {preview && (
                    <div className="relative">
                        <img
                            src={preview}
                            alt="Preview"
                            className="w-full h-48 object-cover rounded-xl border border-green-200"
                        />
                    </div>
                )}

                {/* Button */}
                <button
                    onClick={handleSubmit}
                    disabled={loading || !image}
                    className={`w-full py-3 rounded-xl font-bold text-white transition ${loading || !image
                            ? "bg-gray-400 cursor-not-allowed"
                            : "bg-green-600 hover:bg-green-700 active:scale-95"
                        }`}
                >
                    {loading ? "Predicting..." : "Predict Disease"}
                </button>

                {/* Result */}
                {result && (
                    <div className="bg-green-50 p-4 rounded-xl shadow-inner border border-green-200 animate-fade-in">
                        <p className="font-semibold text-green-800 text-lg">                            Disease: <span className="font-bold text-green-900">{result.class}</span>
                        </p>
                        <p className="text-green-700">
                            Confidence: **{(result.confidence * 100).toFixed(2)}%**
                        </p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default Home