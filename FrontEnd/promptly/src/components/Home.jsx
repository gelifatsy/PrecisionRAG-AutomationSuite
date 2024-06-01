import  'react';
import { Link } from 'react-router-dom';

const Home = () => {
  const containerStyle = {
    height: '90vh', // Set height to full viewport height
    background: 'linear-gradient(to bottom, rgba(25, 65, 133, 1) 0%, rgba(25, 65, 133, 0.8) 100%)', // Adjusted background gradient
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
  };

  return (
    <div className="home-container relative flex flex-col items-center justify-center w-full pt-20" style={containerStyle}>
      <h1 className="home-title text-7xl font-bold text-white leading-tight mb-12">
        Generative AI for Your <br/> Enterprise
      </h1>
      <p className="home-description text-xl text-white w-full mb-8">
        Build tailor-made generative AI agents, applications and chatbots that cater to your users unique needs.<br/> Seamlessly integrate your own data and GPT-powered models without any coding experience.
      </p>
      <div className="button-container flex justify-center">
      <Link to="/promptly">
          <button className="home-button bg-red-500 text-white font-medium rounded-full px-6 py-3 mr-4 hover:bg-red-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 shadow-lg">
            Get Started for Free
          </button>
        </Link>
        <button className="home-button bg-blue-500 text-white font-medium rounded-full px-6 py-3 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 shadow-lg">
          Browse AI Apps
        </button>
      </div>
    </div>
  );
};

export default Home;
