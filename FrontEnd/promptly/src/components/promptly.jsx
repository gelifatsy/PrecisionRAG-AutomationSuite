import { useState } from 'react';

const Promptly = () => {
  const [userInput, setUserInput] = useState('');
  const [prompts, setPrompts] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/gep', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
      });

      const data = await response.json();

      if (data && Array.isArray(data) && data.length > 0) {
        const newPrompts = data.map((item) => ({
          prompt: item.prompt,
          classification: item.classification,
          accuracy: item.accuracy,
          sufficient_context: item.sufficient_context,
        }));
        setPrompts(newPrompts);
      } else {
        console.error('Invalid data format or empty prompts array');
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }

    setLoading(false);
    setUserInput('');
  };
  return (
    <div className="promptly-container flex flex-col items-center h-100vh justify-end bg-lightblue p-8 pt-12">
      <div className="promptly-header flex flex-col items-center w-full mb-8">
        <h1 className="promptly-title text-5xl font-bold text-center text-gray-800 leading-tight mb-4">
          Generative AI for Your <br/> Enterprise
        </h1>
        <p className="promptly-description text-xl text-gray-700 w-full text-center">
          {
            // Combine description text from the original "Chat" component
            <>
              Build tailor-made generative AI agents, applications and chatbots that cater to your users unique needs.<br/>
              Seamlessly integrate your own data and GPT-powered models without any coding experience.
            </>
          }
        </p>
      </div>
      <div className="input-container flex items-center justify-center w-full mb-8 gap-4">
        <textarea
          className="promptly-input rounded-lg px-4 py-3 mb-4 border focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none w-2/5 text-center"
          placeholder="Enter your query..."
          value={userInput}
          onChange={handleInputChange}
          style={{
            // Added shadow styles for 3D effect
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.15), 0px 2px 4px rgba(0, 0, 0, 0.22)',
            transform: 'translateY(4px)',
          }}
        />
        <button
          className="submit-button bg-blue-500 text-white font-medium rounded-full px-12 py-3 shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          onClick={handleSubmit}
        >
          Generate Prompts
        </button>
      </div>
      {loading && <div className="spinner" />} {/* Placeholder for spinner */}
      {prompts.length > 0 && (
        <div className="output-container grid grid-cols-2 gap-4 w-3/4 mt-4">
          {prompts.map((prompt, index) => (
            <div key={index} className="prompt-item bg-white rounded-lg p-4 shadow-md">
              <p className="prompt-text text-lg text-gray-700">{prompt.prompt}</p>
              <p className="accuracy-text text-sm text-gray-500">
                Accuracy: {prompt.accuracy}%
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Promptly;
