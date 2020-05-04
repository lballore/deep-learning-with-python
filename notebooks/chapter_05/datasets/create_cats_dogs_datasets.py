import os
import shutil

# The path to the directory where the original dataset was uncompressed
ORIGINAL_DATASET_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/Kaggle-cats-dogs"

# The directory where we will store our smaller dataset
BASE_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/cats_and_dogs_small"


def main():
    os.mkdir(BASE_DIR)

    # Directories for our training, validation and test splits
    train_dir = os.path.join(BASE_DIR, 'train')
    os.mkdir(train_dir)
    validation_dir = os.path.join(BASE_DIR, 'validation')
    os.mkdir(validation_dir)
    test_dir = os.path.join(BASE_DIR, 'test')
    os.mkdir(test_dir)

    # Directory with our training cat pictures
    train_cats_dir = os.path.join(train_dir, 'cats')
    os.mkdir(train_cats_dir)

    # Directory with our training dog pictures
    train_dogs_dir = os.path.join(train_dir, 'dogs')
    os.mkdir(train_dogs_dir)

    # Directory with our validation cat pictures
    validation_cats_dir = os.path.join(validation_dir, 'cats')
    os.mkdir(validation_cats_dir)

    # Directory with our validation dog pictures
    validation_dogs_dir = os.path.join(validation_dir, 'dogs')
    os.mkdir(validation_dogs_dir)

    # Directory with our validation cat pictures
    test_cats_dir = os.path.join(test_dir, 'cats')
    os.mkdir(test_cats_dir)

    # Directory with our validation dog pictures
    test_dogs_dir = os.path.join(test_dir, 'dogs')
    os.mkdir(test_dogs_dir)

    # Copy first 1000 cat images to train_cats_dir
    fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(train_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Copy next 500 cat images to validation_cats_dir
    fnames = ['cat.{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(validation_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Copy next 500 cat images to test_cats_dir
    fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(test_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Copy first 1000 dog images to train_dogs_dir
    fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(train_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Copy next 500 dog images to validation_dogs_dir
    fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(validation_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Copy next 500 dog images to test_dogs_dir
    fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DATASET_DIR, fname)
        dst = os.path.join(test_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Sanity checks
    print('total training cat images:', len(os.listdir(train_cats_dir)))
    print('total training dog images:', len(os.listdir(train_dogs_dir)))
    print('total validation cat images:', len(os.listdir(validation_cats_dir)))
    print('total validation dog images:', len(os.listdir(validation_dogs_dir)))
    print('total test cat images:', len(os.listdir(test_cats_dir)))
    print('total test dog images:', len(os.listdir(test_dogs_dir)))


if __name__ == "__main__":
    main()
